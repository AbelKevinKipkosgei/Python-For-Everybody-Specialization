import sqlite3

conn = sqlite3.connect("orgdb.sqlite")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Counts")

cur.execute(
    """
CREATE TABLE Counts (org TEXT, count INTEGER)"""
)

file_name = input("Enter file name: ")
if len(file_name) < 1:
    file_name = "mbox.txt"
file_handle = open(file_name)
for line in file_handle:
    if not line.startswith("From: "):
        continue
    pieces = line.split()
    email = pieces[1]
    org = email.split("@")[-1]
    cur.execute(
        """
        SELECT count FROM Counts WHERE org = ?""",
        (org,),
    )
    row = cur.fetchone()
    if row is None:
        cur.execute(
            """
            INSERT INTO Counts (org, count) VALUES (?, 1)""",
            (org,),
        )
    else:
        cur.execute("""UPDATE Counts SET count = count + 1 WHERE org = ?""", (org,))

conn.commit()

sql_string = """
                SELECT org, count FROM Counts ORDER BY count DESC
                """
for row in cur.execute(sql_string):
    print(str(row[0]), row[1])
cur.close()
