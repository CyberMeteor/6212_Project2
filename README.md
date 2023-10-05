# 6212_Project2
CSCI6212 project_2 huffman coding

## Steps to Build a Huffman Tree:
1. Start with an input array of unique characters and their frequencies.
2. Create a leaf node for each unique character and build a min heap (priority queue) with these leaf nodes. The min heap is initially ordered based on the frequency of characters, with the least frequent character at the root.
3. Extract two nodes with the minimum frequency from the min heap. Create a new internal node with a frequency equal to the sum of the frequencies of the two extracted nodes. Make one of the extracted nodes the left child of the new internal node and the other extracted node the right child. Add this new internal node back to the min heap.
4. Repeat steps 2 and 3 until the min heap contains only one node. This remaining node is the root node of the Huffman Tree, and the construction of the tree is complete.

In essence, the algorithm builds the Huffman Tree by repeatedly merging the two nodes with the lowest frequencies into a new internal node until there is only one node left in the heap, which becomes the root of the Huffman Tree.

