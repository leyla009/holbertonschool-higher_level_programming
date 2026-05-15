#!/usr/bin/python3
import os

def generate_invitations(template, attendees):
    """
    Generates personalized invitation files from a template and a list of attendees.
    """
    # Check Input Types
    if not isinstance(template, str):
        print(f"Error: Invalid input type. Template should be a string (got {type(template).__name__}).")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Invalid input type. Attendees should be a list of dictionaries.")
        return

    # Handle Empty Inputs
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process Each Attendee
    for index, attendee in enumerate(attendees, start=1):
        processed_template = template
        
        # Placeholders to replace
        placeholders = ["name", "event_title", "event_date", "event_location"]
        
        for key in placeholders:
            # Get value or "N/A" if missing/None
            value = attendee.get(key)
            if value is None:
                value = "N/A"
            
            # Replace placeholder {key} with the value
            # Using .replace() as per the hints
            processed_template = processed_template.replace(f"{{{key}}}", str(value))
        
        # Generate Output Files
        filename = f"output_{index}.txt"
        
        # Check if file exists to avoid overwriting (optional but recommended in hints)
        if os.path.exists(filename):
            print(f"Warning: {filename} already exists. Overwriting...")

        try:
            with open(filename, 'w') as f:
                f.write(processed_template)
        except Exception as e:
            print(f"Error writing to {filename}: {e}")
