import requests
import time
from urllib.parse import quote

def check_channel_availability(channel_name):
    # Clean the channel name and create URL
    clean_name = channel_name.strip().replace("youtube.com/@", "")
    url = f"https://www.youtube.com/@{quote(clean_name)}"
    
    try:
        # Make request to YouTube
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        
        # Check if channel exists based on response
        if response.status_code == 404:
            return False
        elif response.status_code == 200 and "This page isn't available" not in response.text:
            return True
        else:
            return False
            
    except Exception as e:
        print(f"Error checking {channel_name}: {str(e)}")
        return None

def main():
    # List to store available channel names
    available_channels = []
    
    try:
        # Read channel names from file
        with open('list.txt', 'r', encoding='utf-8') as file:
            channel_names = file.readlines()
        
        # Check each channel
        for channel in channel_names:
            channel = channel.strip()
            if not channel:  # Skip empty lines
                continue
                
            print(f"Checking: {channel}")
            exists = check_channel_availability(channel)
            
            if exists is False:  # Channel doesn't exist
                available_channels.append(channel)
            
            # Add delay to avoid rate limiting
            time.sleep(2)
            
        # Write available channels to output file
        with open('available_channels.txt', 'w', encoding='utf-8') as file:
            for channel in available_channels:
                file.write(f"{channel}\n")
                
        print(f"\nFound {len(available_channels)} available channels!")
        print("Results have been saved to 'available_channels.txt'")
            
    except FileNotFoundError:
        print("Error: '1.txt' file not found!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
