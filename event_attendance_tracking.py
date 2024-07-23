# Event Attendance Tracking
# Scenario: You are managing attendance for a series of events. 
# Each event has a unique ID and a list of attendees. 
# Each attendee has a unique ID and a list of events they attended. 
# You need to find the top attendees who attended the most events and identify which events 
# are the most popular.

# Question: Write a function that takes two dictionaries: 
# one representing events (event IDs as keys and a list of attendee IDs as values) and 
# one representing attendees (attendee IDs as keys and a list of event IDs as values). 
# Return a list of the top attendees (those who attended the most events) and the most 
# popular events (those with the highest number of attendees).

event_details = {"E001": ["A001", "A005", "A006", "A010"],
                 "E002": ["A002", "A003", "A005", "A008", "A009"],
                 "E003": ["A001", "A004", "A006", "A010", "A009"],
                 "E004": ["A001", "A002", "A007"]}

attendee_details = {"A001": ["E001", "E003", "E004"],
                    "A002": ["E002", "E004"],
                    "A003": ["E002"],
                    "A004": ["E003"],
                    "A005": ["E001", "E002"],
                    "A006": ["E001", "E003"],
                    "A007": ["E004"],
                    "A008": ["E002"],
                    "A009": ["E002", "E003"],
                    "A010": ["E001", "E003"]}

def event_attendance(event, attendee):
    top_attendees = []
    popular_event = []
    event_count = float('-inf')
    attendance_count = float('-inf')
    for attendee_id, event_list in attendee.items():
        if len(event_list) > event_count:
            event_count = len(event_list)
            top_attendees.append(attendee_id)
    for event_id, attendee_list in event.items():
        if len(attendee_list) > attendance_count:
            attendance_count=len(attendee_list)
            popular_event = event_id
    return (f"No. of event attended :  {event_count}", f"Attendee ID : {top_attendees}") , (f"No. of attendees : {attendance_count}", f"Popular Event : {popular_event}")
print(event_attendance(event_details, attendee_details))