def user_input():
    try:
        user_input = input("You: ")
        return user_input
    except Exception as e:
        print(f"Error: {e}")