from Process_list import ProcessList

class Escalonador:

    def __init__(self):
        self.high_priority_list = ProcessList()
        self.mediun_priority_list = ProcessList()
        self.low_priority_list = ProcessList()
        self.blocked_list = ProcessList()
        self.high_worst_cycle_counter = 0


    def run_cpu_cycles(self):
        print("=== Início do Ciclo ===")

        if not self.blocked_list.empty():
            processo = self.blocked_list.remove_start()
            self.insert_by_priority(processo)
            print(f"[DESBLOQUEIO] {processo.nome} retornou à fila P{processo.priority}")

        processo = None
        origem = None

        if self.high_worst_cycle_counter >= 5:
            if not self.mediun_priority_list.empty():
                processo = self.mediun_priority_list.remove_start()
                origem = self.mediun_priority_list
                self.high_worst_cycle_counter = 0
                print("[ANTI-INANIÇÃO] Executando processo de prioridade MÉDIA")
            elif not self.low_priority_list.empty():
                processo = self.low_priority_list.remove_start()
                origem = self.low_priority_list
                self.high_worst_cycle_counter = 0
                print("[ANTI-INANIÇÃO] Executando processo de prioridade BAIXA")

        if not processo:
            if not self.high_priority_list.empty():
                processo = self.high_priority_list.remove_start()
                origem = self.high_priority_list
                self.high_worst_cycle_counter += 1
            elif not self.mediun_priority_list.empty():
                processo = self.mediun_priority_list.remove_start()
                origem = self.mediun_priority_list
                self.high_worst_cycle_counter = 0
            elif not self.low_priority_list.empty():
                processo = self.low_priority_list.remove_start()
                origem = self.low_priority_list
                self.high_worst_cycle_counter = 0
            else:
                print("Nenhum processo pronto para executar.")
                return