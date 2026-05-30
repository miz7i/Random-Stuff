import sys
import time

def print_slow(text, delay=0.06):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_simultaneously_stacked_bridge(text1, delay1, text2, delay2, line2_start_delay):
    print("\n\n") 
    
    start_time = time.time()
    
    while True:
        elapsed = time.time() - start_time
      
        chars1 = int(elapsed / delay1)
        line1 = text1[:chars1]
        
        if elapsed > line2_start_delay:
            chars2 = int((elapsed - line2_start_delay) / delay2)
            line2 = text2[:chars2]
        else:
            line2 = ""
            chars2 = 0
      
        sys.stdout.write(f"\033[3F\r{line1}\033[K\n\033[K\n{line2}\033[K\n")
        sys.stdout.flush()
        
        if chars1 >= len(text1) and chars2 >= len(text2):
            break
            
        time.sleep(0.01)

def print_simultaneously_stacked(text1, delay1, text2, delay2):
    sys.stdout.write("\n\n")
    sys.stdout.flush()
    
    start_time = time.time()
    while True:
        elapsed = time.time() - start_time
        chars1 = int(elapsed / delay1)
        chars2 = int(elapsed / delay2)
        
        line1 = text1[:chars1]
        line2 = text2[:chars2]
        
        sys.stdout.write(f"\033[2F\r{line1}\033[K\n{line2}\033[K\n")
        sys.stdout.flush()
        
        if chars1 >= len(text1) and chars2 >= len(text2):
            break
            
        time.sleep(0.01)

def main():
    print("=" * 50)
    print("🎵 Shape of My Heart - Backstreet Boys 🎵")
    print("=" * 50)
    print()

    time.sleep(2.0)

    print_slow("I'm lookin' back on things I've done", 0.13)
    time.sleep(0.6)
    print_slow("I never wanna play the same old part", 0.135)
    time.sleep(0.8)
    print_slow("I'll keep you in the dark", 0.1)
    time.sleep(1.6)
  
    print_simultaneously_stacked_bridge(
        "Now let me show you the shape of my heart", 0.12,
        "Looking back on the things I've done", 0.075,
        4.4
    )
    
    time.sleep(0.99)
    print_slow("I was trying to be someone", 0.13)
    time.sleep(0.3)
    
    print_simultaneously_stacked(
        "(I was trying to be someone)", 0.10,
        "I played my part, kept you in the dark", 0.166
    )
    
    time.sleep(0.7)
    print_slow("Now let me show you the shape of my heart", 0.15)
    time.sleep(4.0)

if __name__ == "__main__":
    main()