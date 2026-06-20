"""
To Differentiate between Errors and Normal Logs
Place the logs in logs.txt
Logs will be differentiated in debug_report.txt, error_report.txt and warning_report.txt according to their level of severity
"""
log_counts = {
    "ERROR": 0,
    "DEBUG": 0,
    "WARNING": 0
}
with open("logs.txt" , "r") as file:
    with open("error_report.txt", "w") as e_file, \
         open("debug_report.txt", "w") as d_file, \
         open("warning_report.txt", "w") as w_file:
        for line in file:
            cline = line.strip()
            if "ERROR" in cline:
                log_counts["ERROR"] +=1;
                e_file.write(cline + "\n")
            if "DEBUG" in cline:
                log_counts["DEBUG"] +=1;
                d_file.write(cline + "\n")
            if "WARNING" in cline:
                log_counts["WARNING"] +=1;
                w_file.write(cline + "\n")

print("Analysis complete")
