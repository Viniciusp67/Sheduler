import sys
from Escalonador import Escalonador
from Process import Process

def validate_file(path):
    errors = []
    with open(path, 'r', encoding='utf-8') as f:
        for num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue

            parts = line.split(',')
            if len(parts) != 5:
                errors.append(f"Line {num}: invalid number of columns (expected: 5, found: {len(parts)})")
                continue

            pid_str, name, prio_str, cycles_str, resource = parts
            try:
                pid = int(pid_str)
                if pid <= 0:
                    errors.append(f"Line {num}: 'pid' must be a positive integer")
            except ValueError:
                errors.append(f"Line {num}: 'pid' must be an integer")

            if not name.strip():
                errors.append(f"Line {num}: 'name' cannot be empty")

            try:
                priority = int(prio_str)
                if priority not in (1, 2, 3):
                    errors.append(f"Line {num}: 'priority' must be 1, 2 or 3")
            except ValueError:
                errors.append(f"Line {num}: 'priority' must be an integer")

            try:
                cycles = int(cycles_str)
                if cycles <= 0:
                    errors.append(f"Line {num}: 'cycles_needed' must be a positive integer")
            except ValueError:
                errors.append(f"Line {num}: 'cycles_needed' must be an integer")

    return errors if errors else None

def load_processes(path):
    scheduler = Escalonador()
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            pid, name, priority, cycles, resource = line.split(',')
            process = Process(
                int(pid),
                name.strip(),
                int(priority),
                int(cycles),
                resource.strip() if resource.strip() else None
            )
            scheduler.insert_by_priority(process)
    return scheduler

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py processes.txt")
        return

    path = sys.argv[1]

    # Validation
    errors = validate_file(path)
    if errors:
        print("Input file error(s):")
        for error in errors:
            print(" -", error)
        return

    try:
        scheduler = load_processes(path)
    except FileNotFoundError:
        print("File not found:", path)
        return

    cycle = 1
    while True:
        print(f"\n--- Cycle {cycle} ---")
        scheduler.display_state()
        scheduler.run_cpu_cycle()

        if (scheduler.high_priority.is_empty() and
            scheduler.medium_priority.is_empty() and
            scheduler.low_priority.is_empty() and
            scheduler.blocked.is_empty()):
            print("\n All processes finished.")
            break

        cycle += 1
        if cycle > 1000:
            print("Cycle limit reached.")
            break

if __name__ == "__main__":
    main()