# File Comparison — Simple Step-by-Step Tasks

## 1. Decide what the program does
Write a short sentence describing the program: for example, "Compare two files to see if they are exactly the same."

## 2. Decide which files to compare
Choose the two files you want to check for identical content.

## 3. Read the files in small parts
Plan to open each file and read it in pieces to handle large files without problems.

## 4. Create a unique code (hash) for each file
Decide to create a unique fingerprint for each file so it can be compared easily.

## 5. Compare the codes
Check whether the fingerprints of the two files are the same or different.

## 6. Show the result to the user
Decide what message to display:
- "These files are identical" if the files match
- "These files are not identical" if the files differ

## 7. Handle errors (optional)
Decide what to do if one or both files cannot be read (for example, show an error message).

## 8. Test the program manually
Try it with identical files and different files to see that the program works correctly.

## Optional extras
- Compare more than two files at once.
- Show which parts of the files are different.
- Use a faster or stronger method for larger files.
- Allow the user to type the file names instead of hardcoding them.