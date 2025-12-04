from pyscript import display, document

def show_info(event):
    output = document.getElementById("output")

    name = document.getElementById("name").value
    contact = document.getElementById("contact").value

    club1 = document.getElementById("sections").value
    club2 = document.getElementById("sections2").value

    info1 = CLUBINFO.get(club1, {})
    info2 = CLUBINFO.get(club2, {})

    summary = f"""
--- Club 1: {club1} ---
Teacher: {info1.get('Teacher')}
Description: {info1.get('Description')}
Meeting Time: {info1.get('Meeting Time')}
Location: {info1.get('Location')}
Members: {info1.get('Number of Members')}

--- Club 2: {club2} ---
Teacher: {info2.get('Teacher')}
Description: {info2.get('Description')}
Meeting Time: {info2.get('Meeting Time')}
Location: {info2.get('Location')}
Members: {info2.get('Number of Members')}

Name: {name}
Contact: {contact}
"""

    display(summary, target="output")


# Attach the listener OUTSIDE the function
document.getElementById("submitBtn").addEventListener("click", show_info)
