# Ex03 Time Table
## Date:23/09/2025

## AIM
To write a html webpage page to display your slot timetable.

## ALGORITHM
### STEP 1
Create a Django-admin Interface.

### STEP 2
Create a static folder and inert HTML code.

### STEP 3
Create a simple table using ```<table>``` tag in html.

### STEP 4
Add header row using ```<th>``` tag.

### STEP 5
Add your timetable using ```<td>``` tag.

### STEP 6
Execute the program using runserver command.

## PROGRAM
```
time.html
time.html
<html>
    <head>
        <title>DHEENADHAYA-25017597</title>
        <center>
            
            <img src="logo.png" width="500" height="200">
            
        <table border="5" height=280 width=280>
           <h2>SLOT TIMETABLE-DHEENADHAYA-25017597</h2>
            
            <tr bgcolor="blue">
                <th>Day/Time</th>
                <th>Monday</th>
                <th>Tuesday</th>
                <th>Wednesday</th>
                <th>Thursday</th>
                <th>Friday</th>
                <th>Saturday</th>
            </tr>
            <tr bgcolor="D9F99D">
                <td bgcolor="blue">8-10</td>
                <td></td>
                <td>CRYPT</td>
                <td>FWAD</td>
                <td>PYTh</td>
                <td></td>
                <td>FWAD</td>
            </tr>
            <tr bgcolor="6D4C41">
                <td bgcolor="blue">10-12</td>
                <td>PYTH</td>
                <td></td>
                <td>FWAD</td>
                <td>PYTH</td>
                <td>CRYPT</td>
                <td>CRYPT</td>
            </tr>
            <tr bgcolor="E9D5FF">
                <td bgcolor="blue">12-1</td>
              <td colspan="6"> <center>LUNCH</center></td>
            </tr>
            <tr bgcolor="#E1BEE7">
                <td bgcolor="blue">1-3</td>
                <td></td>
                <td></td>
                <td></td>
                <td></td>
                <td>FWAD</td>
                <td>FWAD</td>
            </tr>
            <tr bgcolor="80DEEA">
                <td bgcolor="blue">3-5</td>
                <td></td>
                <td>CRYPT</td>
                <td>PYTH</td>
                <td></td>
                <td>PYTH</td>
                <td></td>


            </tr>
            
         
        </table>
        <br>
        <br>
        <table border="5">
            <tr>
                <th>S.NO.</th>
                <th>Subject Code</th>
                <th ><center>Subject Name</center></th>
            </tr>
            <tr>
                <td>1.</td>
                <td>19CS547</td>
                <td>Fundamentals of Cryptocurrency</td>
            </tr>
            <tr>
                <td>2.</td>
                <td>19AI301</td>
                <td>Python Programming</td>
            </tr>
            <tr>
                <td>3.</td>
                <td>19AI414</td>
                <td>Fundamentals of Web Applications Development</td>
            </tr>
        </table>
        <hr>
        </center>
    </head>
</html>

```


## OUTPUT
![alt text](<dheena/Screenshot (21).png>)
![alt text](<dheena/Screenshot (22).png>)


## RESULT
The program for creating slot timetable using basic HTML tags is executed successfully.
