# AI Python-to-C Translator

*This project has been created by [3ka1tz](https://github.com/3ka1tz).*

## Description

This project aims to leverage the well-known performance benefits of the C language without sacrificing the ease and convenience of Python programming. To achieve this, I am developing an AI-powered, leak-free Python-to-C translator.

As Python's popularity continues to grow, many organizations face trade-offs in execution speed and computational efficiency. The relevance of this trade-off is highlighted in a comprehensive study by researchers at the Universidade do Minho in Portugal, which evaluates energy, speed, and memory efficiency across popular programming languages:

![Efficiency comparison table](efficiency-comparison.png)

As the data demonstrates, the efficiency gap between C and Python is substantial, with C consistently ranking as the top-tier option. This project bridges that gap, helping organizations reduce operational costs and minimize environmental emissions.

### Results

Case 1:  
![Data performance test](data_perf.jpg)

Case 2:  
![Math performance test](math_perf.jpg)

Case 3:  
![Text performance text](text_perf.jpg)

## Instructions

1. Update the system
```bash
sudo apt update && sudo apt upgrade -y
```

2. Install curl command
```bash
sudo apt install curl -y
```

3. Install ollama
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

4. Install desired AI model
```bash
ollama run qwen2.5-coder:7b
```

5. Create virtual environment
```bash
python3 -m venv venv
```

6. Activate the virtual environment
```bash
source venv/bin/activate
```

7. Install git command
```bash
sudo apt install git -y
```

8. Clone the repository
```bash
git clone https://github.com/3ka1tz/ai-python-to-c-translator
```

9. Install the requirements
```bash
pip install -r requirements.txt
```

10. Use the translator
```bash
python3 translator.py data_sample.py
```

11. Check the results
```bash
python3 data_perf.py
```

## Resources

- [Cython Documentation](https://cython.readthedocs.io/en/latest)
- [Energy Efficiency across Programming Languages](https://sites.google.com/view/energy-efficiency-languages/home)
- [Ollama Documentation](https://docs.ollama.com)
- [Qwen Models for Ollama](https://ollama.com/library/qwen)
