class SelectiveRepeatARQ:
    def __init__(self, window_size, total_frames):
        self.window_size = window_size
        self.total_frames = total_frames
        self.send_base = 0
        self.next_seq_num = 0
        self.acked = [False] * total_frames  # To track ACK status of each frame
        self.frames = ["Frame " + str(i) for i in range(total_frames)]
    
    def send(self):
        while self.send_base < self.total_frames:
            # Send frames within the window
            for i in range(self.window_size):
                if self.next_seq_num < self.total_frames:
                    print(f"Sending {self.frames[self.next_seq_num]}")
                    self.next_seq_num += 1
            
            # Simulate receiving ACKs
            self.receive_ack()
            
            # Move the window
            while self.send_base < self.total_frames and self.acked[self.send_base]:
                print(f"Sliding window. Frame {self.send_base} acknowledged.")
                self.send_base += 1

    def receive_ack(self):
        # Simulate some ACKs received, and some lost
        for i in range(self.send_base, min(self.send_base + self.window_size, self.total_frames)):
            if not self.acked[i]:  # If not already acknowledged
                ack = input(f"ACK received for {self.frames[i]}? (yes/no): ").strip().lower()
                if ack == "yes":
                    self.acked[i] = True
                    print(f"{self.frames[i]} acknowledged.")
                else:
                    print(f"{self.frames[i]} not acknowledged, will be resent.")

# Example usage
window_size = 4
total_frames = 8
sr_arq = SelectiveRepeatARQ(window_size, total_frames)
sr_arq.send()
