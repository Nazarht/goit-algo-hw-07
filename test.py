from binary_tree import BST
from comment_system import Comment

print("=== Завдання 1-3: BST ===")
bst = BST()
values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]
for value in values:
    bst.insert(value)

print(f"Max: {bst.find_max()}")
print(f"Min: {bst.find_min()}")
print(f"Sum: {bst.sum_all()}")

print("\n=== Завдання 4: Коментарі ===")
root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книга, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

reply1.remove_reply()

root_comment.display()

