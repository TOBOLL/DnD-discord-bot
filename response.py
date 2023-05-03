import random


def handle_response(message) -> str:
    message = message.lower()
    value_message = message.split("d")
    number_throws = int(value_message[0])
    dice_type = int(value_message[1])
    throws = []
    for throw in range(number_throws):
        throws.append(random.randrange(1, dice_type + 1))

    return format_response(throws)


def format_response(throws):
    response = ""
    for throw in throws:
        response = response + f"[{str(throw)}]  "
    response = response + "\n" + "suma: " + str(sum(throws))
    return response
