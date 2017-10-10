default: run

bg:
	geckodriver &

run:
	python main.py
	python hard.py
