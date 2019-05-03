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

using System;
using System.Collections.Generic;
using System.Text;

namespace Multiverse.Tools.WorldEditor
{
    public class CutToClipboardCommand : ICommand
    {
        WorldEditor app;
        List<IWorldObject> list;
        List<IObjectCutCopy> cutList = new List<IObjectCutCopy>();
        List<IWorldContainer> parent = new List<IWorldContainer>();
        ClipboardObject clip;

        public CutToClipboardCommand(WorldEditor worldEditor, List<IWorldObject> list)
        {
            this.app = worldEditor;
            this.clip = worldEditor.Clipboard;
            this.list = list;
        }

        #region ICommand Members

        public bool Undoable()
        {
            return true;
        }

        public void Execute()
        {
            foreach (IWorldObject obj in list)
            {
                if (!(obj is IObjectCutCopy))
                {
                    cutList.Clear();
                    return;
                }
                else
                {
                    cutList.Add(obj as IObjectCutCopy);
                }
            }
            clip.Clear();
            clip.State = ClipboardState.cut;
            foreach (IObjectCutCopy obj in cutList)
            {
                parent.Add(obj.Parent);
                clip.Parents.Add(obj.Parent);
                obj.Parent.Remove(obj);
                obj.Parent = clip;
                clip.Add(obj);
            }
        }

        public void UnExecute()
        {
            int i = 0;
            foreach (IWorldObject obj in cutList)
            {
                (obj as IObjectCutCopy).Parent = parent[i];
                parent[i].Add(obj);
                i++;
            }
        }

        #endregion
    }
}
