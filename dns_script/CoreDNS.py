#!/usr/bin/python3

from Db import *
from Config import *
from Util import *
import time

def generate_corefile():
    startTime = time.time()
    print("Starting process Generate Corefile at %s!" % get_current_time())
    try:
        init_last_domain()

        file = open(corefile_dir, 'w+')
        lines = [".:53 {\n","    log\n", "    errors\n", "    forward . " + dns + "\n"]
        file.writelines(lines)
        file.write("    file /etc/coredns/zones/db.localhost.nowhere")

        result = get_all_domains()

        for row in result:
            domain = row[0]
            count = row[1]
            file.write(" %s" % (domain))
        
        file.write("\n}")
        file.close()
        update_last_domain_id(count)
        print("Finish Generating Corefile at %s!" % get_current_time())
        endTime = time.time()
        print("Time elapsed:", time_elapsed(startTime,endTime) * 1000, "milliseconds")
        print("Number of domains:", count)

    except Exception as e:
        print("Error in regenerating Corefile!")
        print(e)

def update_corefile():
    startTime = time.time()
    print("Starting process Update Corefile at %s!" % get_current_time())
    new_last = 0
    try:
        last_domain_id = int(get_last_domain_id()[0])
        result = get_latest_domain(last_domain_id)
        print("Last domain id: ", str(last_domain_id))

        if len(result) == 0:
            print("No new domain found!")
        else:
            with open(corefile_dir, 'r') as file1:
                file_lines = file1.readlines()
                domain_line = file_lines[4].rstrip("\n")
                # print(result)

                for row in result:
                    domain = row[0]
                    new_last = row[1]
                    domain_line = ''.join([domain_line, ' ', domain])
            
                file_lines[4] = domain_line
                file_lines[5] = "\n}\n"
        
                with open(corefile_dir, 'w') as file2:
                    file2.writelines(file_lines)
                update_last_domain_id(new_last)

            print("New last domain ID:", new_last)
        endTime = time.time()
        print("Finish Updating Corefile!")
        print("Time elapsed:", time_elapsed(startTime,endTime) * 1000, "milliseconds")
        
    except Exception as e:
        print("Error in updating Corefile!")
        print(e)
