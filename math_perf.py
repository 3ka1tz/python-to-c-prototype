import time
import sys

try:
    import math_sample
except ImportError:
    print("❌ Error: 'math_sample.py' not found.")
    sys.exit(1)

try:
    import math_sample_cython
except ImportError:
    print("❌ Error: Compiled extension 'math_sample_cython' not found.")
    print("👉 Remember to run first: python translator.py math_sample.py")
    sys.exit(1)

def run_benchmark():
    iterations = 50_000_000
    print("=" * 60)
    print("⚡ PYTHON VS CYTHON (AI-OPTIMIZED) SPEED BENCHMARK ⚡")
    print(f"Testing a loop with {iterations:,} operations...")
    print("=" * 60)
    print("⏳ Running Standard Python version... Please wait.")
    start_py = time.perf_counter()
    result_py = math_sample.calculate_heavy_sum(iterations)
    end_py = time.perf_counter()
    time_py = end_py - start_py
    print(f"🔴 Standard Python Time: {time_py:.6f} seconds")
    print(f"   Result: {result_py}")
    print("-" * 60)
    print("🚀 Running AI-Optimized Cython version...")
    start_cy = time.perf_counter()
    result_cy = math_sample_cython.calculate_heavy_sum(iterations)
    end_cy = time.perf_counter()
    time_cy = end_cy - start_cy
    print(f"🟢 Cython (AI) Time:     {time_cy:.6f} seconds")
    print(f"   Result: {result_cy}")
    print("-" * 60)
    if result_py != result_cy:
        print("⚠️ Warning: Results do not match!")
        return
    speedup = time_py / time_cy
    time_saved = ((time_py - time_cy) / time_py) * 100
    print("📊 FINAL VERDICT:")
    print(f"The AI-Optimized Cython extension is {speedup:.2f}x FASTER than Standard Python.")
    print(f"Total processing time reduced by {time_saved:.2f}%")
    print("=" * 60)

if __name__ == "__main__":
    run_benchmark()
