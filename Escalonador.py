from Process_list import ProcessList

class Escalonador:
    def __init__(self):
        self.high_priority_list = ProcessList()
        self.medium_priority_list = ProcessList()
        self.low_priority_list = ProcessList()
        self.blocked_list = ProcessList()
        self.high_worst_cycle_counter = 0

    def insert_by_priority(self, process):
        if process.priority == 1:
            self.high_priority_list.insert_end(process)
        elif process.priority == 2:
            self.medium_priority_list.insert_end(process)
        elif process.priority == 3:
            self.low_priority_list.insert_end(process)

    def run_cpu_cycles(self):
        print("=== Início do Ciclo ===")

        if not self.blocked_list.empty():
            process = self.blocked_list.remove_start()
            self.insert_by_priority(process)
            print(f"[Unblock] {process.nome} returned to P{process.priority} queue")

        process = None
        source = None

        if self.high_worst_cycle_counter >= 5:
            if not self.medium_priority_list.empty():
                process = self.medium_priority_list.remove_start()
                source = self.medium_priority_list
                self.high_worst_cycle_counter = 0
                print("[Anti_Starvation] Running Medium priority process")
            elif not self.low_priority_list.empty():
                process = self.low_priority_list.remove_start()
                source = self.low_priority_list
                self.high_worst_cycle_counter = 0
                print("[Anti-Starvation] Running Low priority process")

        if not process:
            if not self.high_priority_list.empty():
                process = self.high_priority_list.remove_start()
                source = self.high_priority_list
                self.high_worst_cycle_counter += 1
            elif not self.medium_priority_list.empty():
                process = self.medium_priority_list.remove_start()
                source = self.medium_priority_list
                self.high_worst_cycle_counter = 0
            elif not self.low_priority_list.empty():
                process = self.low_priority_list.remove_start()
                source = self.low_priority_list
                self.high_worst_cycle_counter = 0   
            else:
                print("No ready process to run.")
                return


        if process.recurso_necessario == "Disc" and not process.ja_bloqueado:
            process.ja_bloqueado = True
            self.blocked_list.insert_end(process)
            print(f"[Block] {process.nome} needs DISC and was blocked.")
            return


        print(f"[Run] Running: {process}")
        process.ciclos_necessarios -= 1

        if process.ciclos_necessarios <= 0:
            print(f"[Finish] {process.nome} finished!")
        else:
            source.insert_end(process)
            print(f"[Requeue] {process.nome} returned to queue")

    def display_state(self):
        print("\n[Queues]")
        print("  High:", self.high_priority_list.display_names())
        print("  Medium:", self.medium_priority_list.display_names())
        print("  Low:", self.low_priority_list.display_names())
        print("  Blocked:", self.blocked_list.display_names())