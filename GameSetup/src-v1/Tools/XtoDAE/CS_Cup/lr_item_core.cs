/********************************************************************

The Multiverse Platform is made available under the MIT License.

Copyright (c) 2012 The Multiverse Foundation

Permission is hereby granted, free of charge, to any person 
obtaining a copy of this software and associated documentation 
files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, 
merge, publish, distribute, sublicense, and/or sell copies 
of the Software, and to permit persons to whom the Software 
is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be 
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES 
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE 
OR OTHER DEALINGS IN THE SOFTWARE.

*********************************************************************/

namespace TUVienna.CS_CUP
{

/** The "core" of an LR item.  This includes a production and the position
 *  of a marker (the "dot") within the production.  Typically item cores 
 *  are written using a production with an embedded "dot" to indicate their 
 *  position.  For example: <pre>
 *     A ::= B * C d E
 *  </pre>
 *  This represents a point in a parse where the parser is trying to match
 *  the given production, and has succeeded in matching everything before the 
 *  "dot" (and hence is expecting to see the symbols after the dot next).  See 
 *  lalr_item, lalr_item_set, and lalr_start for full details on the meaning 
 *  and use of items.
 *
 * @see     java_cup.lalr_item
 * @see     java_cup.lalr_item_set
 * @see     java_cup.lalr_state
 * @version last updated: 11/25/95
 * @author  Scott Hudson
 * translated to C# 08.09.2003 by Samuel Imriska
*/

public class lr_item_core {
   
  /*-----------------------------------------------------------*/
  /*--- Constructor(s) ----------------------------------------*/
  /*-----------------------------------------------------------*/

  /** Full constructor.
   * @param prod production this item uses.
   * @param pos  position of the "dot" within the item.
   */
  public lr_item_core(production prod, int pos)     {
      production_part part;

      if (prod == null)
	throw new internal_error(
	  "Attempt to create an lr_item_core with a null production");

      _the_production = prod;

      if (pos < 0 || pos > _the_production.rhs_length())
	throw new internal_error(
	  "Attempt to create an lr_item_core with a bad dot position");

      _dot_pos = pos;

      /* compute and cache hash code now */
      _core_hash_cache = 13*_the_production.GetHashCode() + pos;

      /* cache the symbol after the dot */
      if (_dot_pos < _the_production.rhs_length())
	{
	  part = _the_production.rhs(_dot_pos);
	  if (!part.is_action())
	    _symbol_after_dot = ((symbol_part)part).the_symbol();
	}
    } 

  /*. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .*/

  /** Constructor for dot at start of right hand side. 
   * @param prod production this item uses.
   */
  public lr_item_core(production prod) : this(prod,0)
    {
      //this(prod,0);
    }

  /*-----------------------------------------------------------*/
  /*--- (Access to) Instance Variables ------------------------*/
  /*-----------------------------------------------------------*/

  /** The production for the item. */
  protected production _the_production;

  /** The production for the item. */
  public production the_production() {return _the_production;}

  /*. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .*/

  /** The position of the "dot" -- this indicates the part of the production 
   *  that the marker is before, so 0 indicates a dot at the beginning of 
   *  the RHS.
   */
  protected int _dot_pos;

  /** The position of the "dot" -- this indicates the part of the production 
   *  that the marker is before, so 0 indicates a dot at the beginning of 
   *  the RHS.
   */
  public int dot_pos() {return _dot_pos;}

  /*. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .*/

  /** Cache of the hash code. */
  protected int _core_hash_cache;

  /*. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .*/

  /** Cache of symbol after the dot. */
  protected symbol _symbol_after_dot = null;

  /*. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .*/

  /** Is the dot at the end of the production? */
  public bool dot_at_end() 
    {
       return _dot_pos >= _the_production.rhs_length();
    }

  /*. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .*/

  /** Return the symbol after the dot.  If there is no symbol after the dot
   *  we return null. */
  public symbol symbol_after_dot()
    {
      /* use the cached symbol */
      return _symbol_after_dot;
    }

  /*. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .*/

  /** Determine if we have a dot before a non terminal, and if so which one 
   *  (return null or the non terminal). 
   */
  public non_terminal dot_before_nt()
    {
      symbol sym;

      /* get the symbol after the dot */
      sym = symbol_after_dot();

      /* if it exists and is a non terminal, return it */
      if (sym != null && sym.is_non_term())
	return (non_terminal)sym;
      else
	return null;
    }

  /*. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .*/

  /** Produce a new lr_item_core that results from shifting the dot one 
   *  position to the right. 
   */
  public lr_item_core shift_core()
    {
      if (dot_at_end()) 
	throw new internal_error(
	  "Attempt to shift past end of an lr_item_core");

      return new lr_item_core(_the_production, _dot_pos+1);
    }

  /*. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .*/

  /** Equality comparison for the core only.  This is separate out because we 
   *  need separate access in a super class. 
   */
  public bool core_equals(lr_item_core other)
    {
      return other != null && 
	     _the_production.Equals(other._the_production) && 
	     _dot_pos == other._dot_pos;
    }

  /*. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .*/

  /** Equality comparison. */
  public bool Equals(lr_item_core other) {return core_equals(other);}

  /*. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .*/

  /** Generic equality comparison. */
  public override bool Equals(object other)
    {
      if (other.GetType()!=typeof(lr_item_core))
	return false;
      else
	return Equals((lr_item_core)other);
    }

  /*. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .*/

  /** Hash code for the core (separated so we keep non overridden version). */
  public int core_hashCode()
    {
      return _core_hash_cache;
    }

  /*. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .*/

  /** Hash code for the item. */
  public override int GetHashCode() 
    {
      return _core_hash_cache;
    }

  /*. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .*/

  /** Return the hash code that object would have provided for us so we have 
   *  a (nearly) unique id for debugging.
   */
  protected int obj_hash()
    {
      return base.GetHashCode();
    }

  /*. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .*/

  /** Convert to a string (separated out from ToString() so we can call it
   *  from subclass that overrides ToString()).
   */
  public string to_simple_string()
    {
      string result;
      production_part part;

      if (_the_production.lhs() != null && 
	  _the_production.lhs().the_symbol() != null &&
	  _the_production.lhs().the_symbol().name() != null)
	result = _the_production.lhs().the_symbol().name();
      else
	result = "$$NULL$$";

      result += " ::= ";

      for (int i = 0; i<_the_production.rhs_length(); i++)
	{
	  /* do we need the dot before this one? */
	  if (i == _dot_pos)
	    result += "(*) ";
	  
	  /* print the name of the part */
	  if (_the_production.rhs(i) == null)
	    {
	      result += "$$NULL$$ ";
	    }
	  else
	    {
	      part = _the_production.rhs(i);
	      if (part == null)
		result += "$$NULL$$ ";
	      else if (part.is_action())
		result += "{ACTION} ";
	      else if (((symbol_part)part).the_symbol() != null &&
                       ((symbol_part)part).the_symbol().name() != null)
		result += ((symbol_part)part).the_symbol().name() + " ";
	      else
		result += "$$NULL$$ ";
	    }
	}

      /* put the dot after if needed */
      if (_dot_pos == _the_production.rhs_length())
	result += "(*) ";

      return result;
    }

  /*. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .*/

  /** Convert to a string */
  public override string ToString() 
    {
      /* can't throw here since super class doesn't, so we crash instead */
      try {
        return to_simple_string();
      } catch(internal_error e) {
	e.crash();
	return null;
      }
    }

  /*-----------------------------------------------------------*/

}
   }
