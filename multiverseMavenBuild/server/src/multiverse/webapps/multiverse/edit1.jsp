<%@ page import="java.sql.*, java.util.*" %>
<html>
<head>
<title>Multiverse</title>
<style>
<!--
td {
	font: 10px verdana, arial narrow, arial, sans-serif;
	margin: 2px 0 10px 0;
	line-height: 1.25em;
	color: #383838;
}

td.white {
	font: 12px verdana, arial narrow, arial, sans-serif;
	margin: 2px 0 10px 0;
	line-height: 1.25em;	
	color: #FFFFFF;
}

a {
	font-family: verdana, arial narrow, arial, sans-serif;
	font-size: 12px;
	font-weight: bold;
	line-height: 1.2em;
	color: #4858FF;
	text-decoration: none;
}

td.head {
	font: 18px arial, sans-serif;
	margin: 2px 0 10px 0;
	line-height: 1.2em;
	color: #FFFFFF;
}

td.copy {
	vertical-align: top;
	font-family: verdana, sans-serif;
	font-size: 9px;
	color: #4C4C4C;
	font-weight: normal;
}	
-->
</style>

</head>

<body background="images/bkgd_sub.gif" bottommargin="0" leftmargin="0" marginheight="0" marginwidth="0" rightmargin="0" topmargin="0">

<!-- Outer table used to center content -->
<table width="100%" border="0" cellspacing="0" cellpadding="0" align="center">
<tr align="center" valign="top">
<td align="center" valign="top">		

<!-- Inner table used to format content -->
<table width="708" border="0" cellspacing="0" cellpadding="0">

<!-- Top row contains logo and spacers -->
<tr align="left" valign="top">
<td align="left" valign="top" rowspan="2"><img src="images/nologo_sub.gif" width="208" height="81" border="0"></td>
<td align="left" valign="top"><img src="images/clear.gif" width="9" height="40" border="0"></td>
<td align="left" valign="top"><img src="images/clear.gif" width="19" height="40" border="0"></td>
<td align="left" valign="top"><img src="images/clear.gif" width="453" height="40" border="0"></td>
<td align="left" valign="top"><img src="images/clear.gif" width="19" height="40" border="0"></td>
</tr>

<!-- Second row contains tab and content label -->		
<tr align="left" valign="top">		
<td align="left" valign="top"><img src="images/clear.gif" width="9" height="41" border="0"></td>
<td align="left" valign="top"><img src="images/left_crnr.gif" width="19" height="41" border="0"></td>
<td align="left" valign="middle" bgcolor="#EFEFEF"><font size="+1">

<!-- Page label goes here -->
Edit User Registration
</font></td>
<td align="left" valign="top"><img src="images/right_crnr.gif" width="19" height="41" border="0"></td>	
</tr>

<!-- Third row contains body text -->
<tr align="left" valign="top">
<td align="left" valign="top" background="images/stripes.gif">
<!--img src="images/clear.gif" width="208" border="0"-->

<!-- Table with labels and entry fields -->
<table>
<form action="offer.html" method="get">
<tr height="8"></tr>
<tr>
<td align="center" class="head">Edit your <br> Multiverse Network <br> account</td>
</tr>

<tr height="8"></tr>
<tr>
<td class="white">Use this page to update your password and other profile data.</td>
</tr>

<tr height="8"></tr>
</form>
</table>

</td>
<td align="left" valign="top"><img src="images/clear.gif" width="9" border="0"></td>			
<td align="left" valign="top" bgcolor="#EFEFEF"><img src="images/grey.gif" width="19" border="0"></td>
<td align="left" valign="top" bgcolor="#EFEFEF">


<%
    String connectString = getServletContext().getInitParameter("connect-string");
    String dbuser = getServletContext().getInitParameter("username");
    String dbpassword = getServletContext().getInitParameter("password");

    String editing = request.getParameter("editing");
    String username = request.getParameter("username");
    if (username == null) {
        username = "";
    }
    String password = request.getParameter("password");
    if (password == null) {
        password = "";
    }
    String password2 = request.getParameter("password2");
    if (password2 == null) {
        if (editing == null) {
            password2 = password;
        }
        else {
            password2 = "";
        }
    }
    String email = request.getParameter("email");
    if (email == null) {
        email = "";
    }

    // Make sure database is operational
    // The newInstance() call is a work around for some 
    // broken Java implementations
    Class.forName("com.mysql.jdbc.Driver").newInstance();
    Connection con = DriverManager.getConnection(connectString, dbuser, dbpassword);
    if (con == null) {
        // transfer to JSP for database error
	pageContext.forward("/dberror.html");
        return;
    }

    // validate initial username and password
    boolean usernameOK = true;
    if (editing == null) {
        // make sure user name exists
        Statement stmt = con.createStatement();
        String query = "SELECT username, password, email FROM user WHERE username = '" +
                username +
                "' and password = '" +
                password +
                "'";

        ResultSet rs = stmt.executeQuery(query);
        if(rs.next()){
            // User name does exist
            username = rs.getString(1);
            password = rs.getString(2);
            email = rs.getString(3);
        }
        else {
            // transfer back to signin JSP
            pageContext.forward("/signin.jsp");
            return;
        }

        // Clean up database
        if(rs != null) rs.close();
        if(stmt != null) stmt.close();
    }

    // validate password
    boolean passwordOK = true;
    String passwordHelp = "";
    int passwordLength = password.length();

    boolean passwordInvalid = false;
    for (int i=0; i < passwordLength; i++) {
        if (!Character.isLetter(password.charAt(i)) &&
            !Character.isDigit(password.charAt(i))) {
            passwordInvalid = true;
            break;
        }
    }

    if (editing == null) {
        passwordHelp = "<br>(Password must contain between 4 & 16 letters or numbers.)";
        passwordOK = false;
    }
    else if (passwordLength == 0) {
        passwordHelp = "<br><font color=\"FF0000\">** (Password missing.  It must contain between 4 & 16 letters or numbers.)";
        passwordOK = false;
    }
    else if (passwordInvalid) {
        passwordHelp = "<br><font color=\"FF0000\">** (Password must contain only letters and numbers.)</font>";
        passwordOK = false;
    }
    else if (passwordLength < 4 || passwordLength > 16) {
        passwordHelp = "<br><font color=\"FF0000\">** (Password must be between 4 & 16 letters or numbers.)</font>";
        passwordOK = false;
    }

    // validate password2
    boolean password2OK = true;
    String password2Help = "";

    if (editing != null &&
        !password.equals(password2)) {
        password2Help = "<br><font color=\"FF0000\">** (Passwords are not the same.)</font";
        password2OK = false;
    }

    // validate email
    boolean emailOK = true;
    String emailHelp = "";
    int emailLength = email.length();

    if (editing == null) {
        emailHelp = "<br>(e.g., johndoe@domain_name.com)";
        emailOK = false;
    }
    else if (emailLength == 0) {
        emailHelp = "<br><font color=\"FF0000\">** (eMail address missing.)";
        emailOK = false;
    }
    else if (email.indexOf('@') < 0 ||
             email.indexOf('.') < 0) {
        emailHelp = "<br><font color=\"FF0000\">** (Invalid email address.)</font>";
        emailOK = false;
    }

    // See if all user data OK
    if (editing != null &&
        usernameOK &&
        passwordOK &&
        password2OK &&
        emailOK ) {

        // See if update succeeds
        int rows = 0;
        Statement stmt = con.createStatement();
        String update = "UPDATE user SET password = '" +
                        password +
                        "', email = '" +
                        email +
                        "' WHERE username = '" +
                        username +
                        "'";

        rows = stmt.executeUpdate(update);

        // Clean up database
        if(stmt != null) stmt.close();

        // See if insert was successful
        if (rows >= 1) {
            // transfer to success JSP
            pageContext.forward("/download.html");
            return;
        }
    }

    // Clean up database
    if(con != null) con.close();

    // Set instructions for form
    String formHelp = "";
    if( editing == null ) {
        formHelp = "Make changes in the form below to update your account.";
    }
    else {
        formHelp = "Fix errors <font color=\"FF0000\">(highlighted in red)</font> and resubmit form.";
    }

%>

<!-- Body text here -->
<%= formHelp %>

<!-- Table with labels and entry fields -->
<table>
<form action="edit1.jsp" method="post">
<input type="hidden" name="username" value="<%= username %>">
<input type="hidden" name="editing" value="yes">
<tr height="8"></tr>

<tr>
<td align="right" valign="top"><strong>User Name:</strong></td>
<td><strong><%= username %></strong></td>
</tr>
<tr height="8"></tr>

<tr>
<td align="right" valign="top"><strong>Password:</strong></td>
<td><input type="password" name="password" maxlength="15" size="15" value="<%= password %>">
<%= passwordHelp %></td>
</tr>
<tr height="8"></tr>

<tr>
<td align="right" valign="top"><strong>Re-Type Password:</strong></td>
<td><input type="password" name="password2" maxlength="15" size="15" value="<%= password2 %>">
<%= password2Help %></td>
</tr>
<tr height="8"></tr>

<tr>
<td align="right" valign="top"><strong>eMail Address:</strong></td>
<td><input type="text" name="email" maxlength="30" size="20" value="<%= email %>">
<%= emailHelp %></td>
</tr>
<tr height="8"></tr>

<tr>
<td></td><td><input type="submit" value="Submit"></td>
</tr>
<tr height="8"></tr>
</form>
</table>

<!-- Links here -->
<a href="tech.html">technology</a>  |  
<a href="team.html">team </a>  |  
<a href="work.html">cool place</a>	
</td>

<td align="left" valign="top" bgcolor="#EFEFEF"><img src="images/grey.gif" width="19" border="0"></td>
</tr>					
</table></td>

<!-- Spacer in next to bottom row of outer table -->
</tr>	
<tr align="center" valign="top" bgcolor="#060F0A">
<td align="center" valign="top"><img src="images/clear.gif" width="100%" height="60" border="0"></td>
</tr>

<!-- Copyright message in bottom row of outer table -->
<tr align="center" valign="top">
<td align="center" valign="top" class="copy"><br>&copy; Copyright Multiverse Network 2005. All rights reserved.</td>
</tr>						
</table>

</body>
</html>
