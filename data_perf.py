import time
import sys

try:
    import data_sample
except ImportError:
    print("❌ Error: 'data_sample.py' not found.")
    sys.exit(1)

try:
    import data_sample_cython
except ImportError:
    print("❌ Error: Compiled extension 'data_sample_cython' not found.")
    print("👉 Remember to run first: python translator.py data_sample.py")
    sys.exit(1)

def run_data_benchmark():
    size = 10_000
    print("=" * 60)
    print("⚡ DATA STRUCTURE BENCHMARK: BUBBLE SORT ALGORITHM ⚡")
    print(f"Sorting an inverted list of {size:,} elements...")
    print("=" * 60)
    print("⏳ Running Standard Python sort... Please wait.")
    py_list = list(range(size, 0, -1))
    start_py = time.perf_counter()
    result_py = data_sample.bubble_sort(py_list)
    end_py = time.perf_counter()
    time_py = end_py - start_py
    print(f"🔴 Standard Python Time: {time_py:.6f} seconds")
    print("-" * 60)
    print("🚀 Running AI-Optimized Cython sort...")
    cy_list = list(range(size, 0, -1))
    start_cy = time.perf_counter()
    result_cy = data_sample_cython.bubble_sort(cy_list)
    end_cy = time.perf_counter()
    time_cy = end_cy - start_cy
    print(f"🟢 Cython (AI) Time:     {time_cy:.6f} seconds")
    print("-" * 60)
    if result_py != result_cy:
        print("⚠️ Warning: Sorted outputs do not match!")
        return
    speedup = time_py / time_cy
    time_saved = ((time_py - time_cy) / time_py) * 100
    print("📊 DATA STRUCTURE EFFICIENCY VERDICT:")
    print(f"🔹 SPEEDUP: Cython is {speedup:.2f}x FASTER (Time reduced by {time_saved:.2f}%).")
    print("=" * 60)

if __name__ == "__main__":
    run_data_benchmark()
