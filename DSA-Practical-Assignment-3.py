# IT12 Data Structure and Algorithms - Practical Assignment 3
# Name: Omkar Nandu Kamble        Roll No: 2601093
#
# Q.1 Hospital Emergency Management
# Manage patients in a hospital using a Priority Queue
# Priority: 1 = Critical, 2 = Serious, 3 = Normal (lower number = treated first)

import heapq
from itertools import count

PRIORITY_LABELS = {1: "Critical", 2: "Serious", 3: "Normal"}


class HospitalQueue:
    def __init__(self):
        self.heap = []           # min-heap of (priority, arrival_order, id, name)
        self.counter = count()   # arrival order -> FIFO among equal priorities
        self.ids = set()         # to prevent duplicate patient IDs

    # 1. Add Patient (enqueue)
    def enqueue(self, patient_id, name, priority):
        if priority not in PRIORITY_LABELS:
            print("Invalid priority! Use 1 (Critical), 2 (Serious) or 3 (Normal).")
            return
        if patient_id in self.ids:
            print(f"Patient ID {patient_id} already exists in the queue.")
            return
        heapq.heappush(self.heap, (priority, next(self.counter), patient_id, name))
        self.ids.add(patient_id)
        print(f"Patient '{name}' (ID: {patient_id}) added as "
              f"{PRIORITY_LABELS[priority]}.")

    # 2. Display the next patient to be treated (display_next)
    def display_next(self):
        if not self.heap:
            print("No patients waiting.")
            return
        priority, _, pid, name = self.heap[0]
        print("Next patient to be treated:")
        print(f"  ID: {pid} | Name: {name} | Priority: {priority} "
              f"({PRIORITY_LABELS[priority]})")

    # 3. Remove a patient from the queue after treatment (dequeue)
    def dequeue(self):
        if not self.heap:
            print("No patients to treat. Queue is empty.")
            return None
        priority, _, pid, name = heapq.heappop(self.heap)
        self.ids.discard(pid)
        print(f"Treated and removed: ID: {pid} | Name: {name} | "
              f"Priority: {priority} ({PRIORITY_LABELS[priority]})")
        return pid

    # 4. Display all waiting patients in priority order (display_all)
    def display_all(self):
        if not self.heap:
            print("No patients waiting.")
            return
        print(f"{'No.':<5}{'ID':<10}{'Name':<20}{'Priority':<10}")
        print("-" * 45)
        for i, (priority, _, pid, name) in enumerate(sorted(self.heap), 1):
            print(f"{i:<5}{pid:<10}{name:<20}{priority} ({PRIORITY_LABELS[priority]})")


def main():
    hospital = HospitalQueue()

    while True:
        print("\n===== Hospital Emergency Management =====")
        print("1. Add Patient")
        print("2. Display Next Patient")
        print("3. Treat / Remove Patient")
        print("4. Display All Waiting Patients")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            pid = input("Enter patient ID: ").strip()
            name = input("Enter patient name: ").strip()
            try:
                priority = int(input("Enter priority (1-Critical, 2-Serious, 3-Normal): "))
            except ValueError:
                print("Priority must be a number (1, 2 or 3).")
                continue
            hospital.enqueue(pid, name, priority)
        elif choice == "2":
            hospital.display_next()
        elif choice == "3":
            hospital.dequeue()
        elif choice == "4":
            hospital.display_all()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()