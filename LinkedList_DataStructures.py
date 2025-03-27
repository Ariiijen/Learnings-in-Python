{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPlWAF2IEz9pvf7IfLSk/yh",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Ariiijen/Learnings-in-Python/blob/main/LinkedList_DataStructures.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-cTUhqVybVYR",
        "outputId": "a8452bc8-6ed1-4910-e2a6-7fe68a611617"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "LinkedList contents: [5, 4, 7, 6]\n",
            "Converted to tuple: (5, 4, 7, 6)\n",
            "Converted to set: {4, 5, 6, 7}\n",
            "Converted to string: 5476\n"
          ]
        }
      ],
      "source": [
        "class Node:\n",
        "    def __init__(self, data):\n",
        "        self.data = data\n",
        "        self.next = None\n",
        "\n",
        "class LinkedList:\n",
        "    def __init__(self, iterable=None):\n",
        "        self.head = None\n",
        "        if iterable:\n",
        "            self.from_iterable(iterable)\n",
        "\n",
        "    def from_iterable(self, iterable):\n",
        "        if isinstance(iterable, (list, tuple, set, str, dict)):\n",
        "            for item in iterable:\n",
        "                self.append(item)\n",
        "        else:\n",
        "            raise TypeError(\"Unsupported data structure\")\n",
        "\n",
        "    def append(self, data):\n",
        "        new_node = Node(data)\n",
        "        if not self.head:\n",
        "            self.head = new_node\n",
        "            return\n",
        "        current = self.head\n",
        "        while current.next:\n",
        "            current = current.next\n",
        "        current.next = new_node\n",
        "\n",
        "    def display(self):\n",
        "        current = self.head\n",
        "        elements = []\n",
        "        while current:\n",
        "            elements.append(current.data)\n",
        "            current = current.next\n",
        "        return elements\n",
        "\n",
        "    def to_list(self):\n",
        "        return self.display()\n",
        "\n",
        "    def to_tuple(self):\n",
        "        return tuple(self.display())\n",
        "\n",
        "    def to_set(self):\n",
        "        return set(self.display())\n",
        "\n",
        "    def to_string(self):\n",
        "        return ''.join(str(item) for item in self.display())\n",
        "\n",
        "    def to_dict(self):\n",
        "        elements = self.display()\n",
        "        if len(elements) % 2 != 0:\n",
        "            raise ValueError(\"Cannot convert to dictionary, odd number of elements\")\n",
        "        return dict(zip(elements[::2], elements[1::2]))\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    ll = LinkedList([5, 4, 7, 6])\n",
        "    print(\"LinkedList contents:\", ll.display())\n",
        "    print(\"Converted to tuple:\", ll.to_tuple())\n",
        "    print(\"Converted to set:\", ll.to_set())\n",
        "    print(\"Converted to string:\", ll.to_string())"
      ]
    }
  ]
}