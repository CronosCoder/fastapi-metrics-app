import psutil
import time
from prometheus_client import Gauge, Counter

cpu_usage = Gauge("custom_process_cpu_seconds_total", "Total CPU time consumed by the process")
memory_rss = Gauge("custom_process_resident_memory_bytes", "Physical memory in bytes")
memory_vms = Gauge("custom_process_virtual_memory_bytes", "Virtual memory in bytes")
open_fds = Gauge("custom_process_open_fds", "Number of open file descriptors")
threads = Gauge("custom_process_num_threads", "Number of threads used")
gc_collections = Counter("custom_process_gc_collections_total", "Number of GC collections")
uptime = Gauge("custom_process_uptime_seconds", "Process uptime in seconds")
start_time = time.time()

def collect_system_metrics():
    process = psutil.Process()
    cpu_usage.set(process.cpu_times().user)
    memory_info = process.memory_info()
    memory_rss.set(memory_info.rss)
    memory_vms.set(memory_info.vms)
    open_fds.set(process.num_fds())
    threads.set(process.num_threads())
    uptime.set(time.time() - start_time)
