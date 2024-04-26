import os
import subprocess

def run_smartbugs(file_path):
    smartbugs_path = "./smartbugs/smartbugs"
    command = f"{smartbugs_path} -t slither -f {file_path} --processes 2 --mem-limit 8g --timeout 600"
    subprocess.run(command, shell=True)

def main():
    directory = "smartbugs/dataset/unchecked_low_level_calls"
    # "smartbugs/dataset/arithmetic"
    # "smartbugs/dataset/bad_randomness"
    # "smartbugs/dataset/denial_of_service"
    # "smartbugs/dataset/short_addresses"
    results_dir = "results"
    sol_files = [file for file in os.listdir(directory) if file.endswith(".sol")]
    for sol_file in sol_files:
        file_path = os.path.join(directory, sol_file)
        run_smartbugs(file_path)
        subprocess.run(f"./smartbugs/reparse {results_dir}", shell=True)
        subprocess.run(f"./smartbugs/results2csv -p {results_dir} > results.csv", shell=True)

if __name__ == "__main__":
    main()
