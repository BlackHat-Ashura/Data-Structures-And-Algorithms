class PlateStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def show(self):
        print(self.stacks, "\n")

    def push(self, value):
        if len(self.stacks) > 0 and len(self.stacks[-1]) < self.capacity:
            self.stacks[-1].append(value)
            print(f"[+] Successfully added {value} to Stack {len(self.stacks)}.\n")
        else:
            self.stacks.append([value])
            print("[+] New Stack created due to StackOverflow.")
            print(f"[+] Successfully added {value} to Stack {len(self.stacks)}.\n")

    def pop(self):
        if not len(self.stacks):
            print("[!] Stack doesn't exist.\n")
        else:
            value = self.stacks[-1].pop()
            if not len(self.stacks[-1]):
                self.stacks.pop()
            return value

    def pop_at(self, stackNum):
        if stackNum > len(self.stacks):
            print(f"[!] Stack {stackNum} doesn't exist.\n")
        else:
            if not len(self.stacks[stackNum - 1]):
                print("[!] Stack doesn't exist.\n")
            else:
                value = self.stacks[stackNum - 1].pop()
                if not len(self.stacks[stackNum - 1]):
                    self.stacks.pop(stackNum - 1)
                return value


# PS = PlateStack(2)
# PS.push(1)
# PS.push(2)
# PS.push(3)
# PS.push(4)
# PS.push(5)
# PS.push(6)
# PS.push(7)
# PS.pop_at(2)
# PS.show()
# PS.pop_at(5)
# PS.show()
