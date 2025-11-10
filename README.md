# Insertion Sort Visualizer using Python Tkinter

This project is a **visual representation of the Insertion Sort algorithm** created using **Python's Tkinter GUI library**. Users can input their own list of numbers, and the program animates the sorting process step-by-step with colored bars, making it easier to understand how the algorithm works internally.

---

## 🚀 Features

* 🔢 **User Input Support** – Enter any custom list of numbers.
* 🎨 **Color-Coded Visualization**:

  * **Red** → Current key element
  * **Yellow** → Shifting elements
  * **Blue** → Unsorted elements
  * **Green** → Correctly placed / Sorted elements
* 🖥️ **Real-time animations** showing each shift and insertion.
* 🧠 **Educational tool** for understanding how Insertion Sort works internally.

---

## 📌 How Insertion Sort Works

Insertion Sort builds the final sorted list **one element at a time**. It takes each element from the unsorted portion and inserts it into the correct position in the sorted portion by shifting larger values to the right.

### Steps:

1. Start from index 1 as the key element.
2. Compare key with elements from right to left in the sorted section.
3. Shift elements that are greater than the key.
4. Insert the key in its correct position.
5. Repeat for all elements.

---

## 📂 Project Structure

```
InsertionSortVisualizer/
│
├── insertion_sort_visualizer.py   # Main program file
├── README.md                      # Project documentation
```

---

## 🛠️ Requirements

* Python 3.x
* Tkinter (comes pre-installed with Python)

---

## ▶️ How to Run

1. Clone the repository:

```
git clone https://github.com/yourusername/insertion-sort-visualizer.git
```

2. Navigate to the folder:

```
cd insertion-sort-visualizer
```

3. Run the program:

```
python insertion_sort_visualizer.py
```

---

## 📷 Screenshots

(Add screenshots of your visualizer here)

---

## 📊 Time & Space Complexity

| Case         | Time Complexity |
| ------------ | --------------- |
| Best Case    | O(n)            |
| Average Case | O(n²)           |
| Worst Case   | O(n²)           |

**Space Complexity:** O(1) – In-place sorting algorithm

---

## ⭐ Why This Project?

This visualizer is perfect for:

* Students learning sorting algorithms
* Educators teaching DSA concepts
* Anyone wanting to understand how Insertion Sort works internally
* Beginners exploring GUI programming in Python

---

## ❤️ Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## 📜 License

This project is open-source under the **MIT License**.

---

## 🙏 Acknowledgments

Thanks for checking out the project! If you liked it, consider giving the repository a ⭐ on GitHub.
