import matplotlib.pyplot as plt

test_results = {398: 'FAILED', 394: 'PASSED', 393: 'PASSED', 392: 'PASSED', 390: 'PASSED', 389: 'PASSED', 387: 'PASSED', 386: 'PASSED', 385: 'PASSED', 384: 'FAILED'}

colors = {"FAILED": "red", "PASSED": "green", "SKIPPED": "yellow"}

plt.figure(figsize=(6.4, 2.4))

for i, result in enumerate(test_results.values()):
    plt.scatter(i, 0, c=colors[result], s=100, edgecolors='black')

plt.xticks(range(len(test_results)), test_results.keys())
plt.gca().axes.get_yaxis().set_visible(False)
plt.title("Test results")
plt.show()