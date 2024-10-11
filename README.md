The virtual whiteboard is a Python-based application that allows users to simulate a collaborative workspace where actions (such as drawing or erasing) can be tracked, and collaboration requests can be managed in a queue. The application uses a simple command-line interface to interact with users, allowing them to perform various tasks like adding actions, undoing the last action, and processing collaboration requests.

Key Features:

•	Participants Management: The program maintains a list of participants in the whiteboard session.
•	Action Management: Users can add new actions to the whiteboard (e.g., drawing, erasing) and undo the last action.
•	Collaboration Requests: The program allows users to add and process collaboration requests in the form of a queue.
•	Undo Functionality: Users can undo the last performed action on the whiteboard.
•	Command-Line Interaction: The program provides an interactive CLI menu for users to manage the whiteboard, actions, and collaboration requests.

Core Functionalities:

1.	Display Participants: Shows a list of all current participants in the session.
2.	Add Action: Allows users to add new actions (e.g., "draw line", "erase text") to the whiteboard.
3.	Undo Last Action: Reverts the last added action.
4.	Add Collaboration Request: Enqueues collaboration requests, such as "Participant X requesting to join."
5.	Process Collaboration Request: Dequeues and processes the next collaboration request.
6.	Display Actions: Lists all current actions performed on the whiteboard.
7.	Display Collaboration Requests: Lists all pending collaboration requests.

