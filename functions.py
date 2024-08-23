from sms_sender import SMSSender  # Import the SMSSender class


def send_sms(sms_msg="You send an empty message!"):
    """
    Purpose: send sms messages
    """
    
    # Initialize SMSSender
    sms_sender = SMSSender()    
    
    # send sms
    sms_sender.send_sms(sms_msg)    
    
# end def

