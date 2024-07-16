#task1
def log_fitness_activities():
    activities = []
    durations = []

    while True:
        activity = input("Enter the fitness activity (or type 'done' to finish): ").capitalize()
        if activity.lower() == 'done':
            break
        duration = int(input(f"Enter the duration in minutes for {activity}: "))
        activities.append(activity)
        durations.append(duration)
        print(f"Logged: {activity} for {duration} minutes.")

    return activities, durations

def main():
    print("Welcome to the Fitness Tracker!")
    activities, durations = log_fitness_activities()
    print("\nLogged Fitness Activities:")
    for activity, duration in zip(activities, durations):
        print(f"{activity}: {duration} minutes")

if __name__ == "__main__":
    main()



#task2
def estimate_calories_burned(activity, duration):
    """
    Estimates the total calories burned based on the activity and its duration.
    
    Parameters:
    activity (str): The type of activity performed.
    duration (int): The duration of the activity in minutes.
    
    Returns:
    float: The estimated total calories burned.
    """
    # The factor of 3.5 calories per minute is used here as a placeholder
    # Different activities can have different factors; here we use a generic one
    calories_per_minute = 3.5
    total_calories = duration * calories_per_minute
    return total_calories

def main():
    # Example activities and durations
    activities = [
        {'activity': 'Running', 'duration': 30},
        {'activity': 'Cycling', 'duration': 45},
        {'activity': 'Swimming', 'duration': 60},
    ]

    for act in activities:
        activity = act['activity']
        duration = act['duration']
        calories_burned = estimate_calories_burned(activity, duration)
        print(f"Activity: {activity}, Duration: {duration} minutes, Calories Burned: {calories_burned} calories")

if __name__ == "__main__":
    main()



#task3
def estimate_calories_burned(activity, duration):
    """
    Estimates the total calories burned based on the activity and its duration.
    
    Parameters:
    activity (str): The type of activity performed.
    duration (int): The duration of the activity in minutes.
    
    Returns:
    float: The estimated total calories burned.
    """
    # The factor of 3.5 calories per minute is used here as a placeholder
    # Different activities can have different factors; here we use a generic one
    calories_per_minute = 3.5
    total_calories = duration * calories_per_minute
    return total_calories

def summary_report(activities):
    """
    Provides a summary report of all activities and total calories burned for the day.
    
    Parameters:
    activities (list of dict): A list of activities with their durations.
    
    Returns:
    str: A summary report of all activities and total calories burned.
    """
    total_calories_burned = 0
    report = "Summary Report:\n"
    report += "-" * 30 + "\n"
    
    for act in activities:
        activity = act['activity']
        duration = act['duration']
        calories_burned = estimate_calories_burned(activity, duration)
        total_calories_burned += calories_burned
        report += f"Activity: {activity}, Duration: {duration} minutes, Calories Burned: {calories_burned:.2f} calories\n"
    
    report += "-" * 30 + "\n"
    report += f"Total Calories Burned: {total_calories_burned:.2f} calories\n"
    
    return report

def main():
    # Example activities and durations
    activities = [
        {'activity': 'Running', 'duration': 30},
        {'activity': 'Cycling', 'duration': 45},
        {'activity': 'Swimming', 'duration': 60},
    ]

    # Generate the summary report
    report = summary_report(activities)
    print(report)

if __name__ == "__main__":
    main()
