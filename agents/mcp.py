from datetime import datetime


def create_mcp_message(sender, receiver, message_type, content):
    return {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "sender": sender,
        "receiver": receiver,
        "message_type": message_type,
        "content": content
    }


def add_mcp_trace(trace, sender, receiver, message_type, content):
    message = create_mcp_message(
        sender=sender,
        receiver=receiver,
        message_type=message_type,
        content=content
    )

    trace.append(message)

    return trace
