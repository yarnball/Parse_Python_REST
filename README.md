# Parse_Python_REST
Use Python to batch delete objects from Parse.com

This is very handy for batch deleting a number of objects in one go. Using Regex, you can type in a string for Python to "find" and give as results. The file will query the regex (eg finding all items that start with "wherethisappears") and return results as json. The second "part" of the code will read the results, and delete objects where they appear. This means the API has to be called twice.


Use the "Results_Only.py" to see only the first part of the code (ie this only queries the objects, and gives you a list of results). Use this to safely check which objects would be deleted using the Regex before acutlaly deleteing the rows.


You'll need to:
1. Define your class

2. Define what you want "Regex" to find

3. Define the collumn for Regex to look in
