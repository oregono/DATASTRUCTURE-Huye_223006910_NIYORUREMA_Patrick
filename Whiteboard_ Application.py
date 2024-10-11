from collections import deque
actions_stack = []
collab_requests_queue = deque()


participants_list = ['Tinox', 'Blander', 'Kamotera']
 

def display_participants():
    print("\nParticipants:")
    for participant in participants_list:
        print(f"- {participant}")


def add_action(action):
    actions_stack.append(action)
    print(f"Action added: {action}")


def undo_last_action():
    if actions_stack:
        last_action = actions_stack.pop()
        print(f"Undone action: {last_action}")
    else:
        print("No actions to undo.")


def add_collaboration_request(request):
    collab_requests_queue.append(request)
    print(f"Collaboration request added: {request}")


def process_collaboration_request():
    if collab_requests_queue:
        next_request = collab_requests_queue.popleft()
        print(f"Processing collaboration request: {next_request}")
    else:
        print("No collaboration requests to process.")


def display_actions():
    if actions_stack:
        print("\nCurrent Drawing Actions:")
        for action in actions_stack:
            print(f"- {action}")
    else:
        print("No actions to display.")


def display_collaboration_requests():
    if collab_requests_queue:
        print("\nCollaboration Requests:")
        for request in collab_requests_queue:
            print(f"- {request}")
    else:
        print("No collaboration requests to display.")


def virtual_whiteboard():
    while True:
        print("\n1. Display Participants")
        print("2. Add Action to Whiteboard")
        print("3. Undo Last Action")
        print("4. Add Collaboration Request")
        print("5. Process Next Collaboration Request")
        print("6. Display All Actions")
        print("7. Display Collaboration Requests")
        print("8. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            display_participants()
        elif choice == '2':
            action = input("Enter action to add (e.g., draw line, erase text): ")
            add_action(action)
        elif choice == '3':
            undo_last_action()
        elif choice == '4':
            request = input("Enter collaboration request (e.g., Request to join by Participant X): ")
            add_collaboration_request(request)
        elif choice == '5':
            process_collaboration_request()
        elif choice == '6':
            display_actions()
        elif choice == '7':
            display_collaboration_requests()
        elif choice == '8':
            print("Exiting the whiteboard.")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    virtual_whiteboard()
