#!/usr/bin/python3
"""
Assignment 2:
Eddie Wang, 10136634
CISC 235, Data Structures
"""

class BinaryTreeVertex:
  def __init__(self, value, left = None, right = None):
    self.right = right
    self.left = left
    self.value = value

class BinarySearchTree:
  def __init__(self, root = None):
    self.root = root
