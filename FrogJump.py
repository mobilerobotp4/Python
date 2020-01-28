'''
Frog Jump (LeetCode 403)
A frog is crossing a river. The river is divided into  x  units and at each unit there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions in sorted ascending order, determine if the forg will be able to cross the river by landing on the last stone. Initially the frog is on the first stone and assume the first jump must be  1  unit.

If the frog's last jump was  k  units, then the next jump must be  k−1 ,  k  or  k+1  units. Note that the frog can only jump in the forward direction.
'''
def CanCrossRiver(stone_positions):
  stack = []
  stack.append((0, 1)) # (position, mean_jump_length)

  end_stone_index = stone_positions[-1]
  while stack:
    position_index, mean_jump_length = stack.pop()
    for jump in range(mean_jump_length-1, mean_jump_length+2):
      if jump <= 0:
        continue
      
      next_position_index = position_index + jump

      if next_position_index == end_stone_index:
        return True

      if next_position_index in stone_positions:
        stack.append((next_position_index, jump))
        print(stack)

  return False
'''
stone_positions = [0, 1, 3, 5, 6, 8, 12, 17]
answer = CanCrossRiver(stone_positions)
print(answer)
[(1, 1)]
[(3, 2)]
[(5, 2)]
[(5, 2), (6, 3)]
[(5, 2), (8, 2)]
[(6, 1)]
[(6, 1), (8, 3)]
[(6, 1), (12, 4)]
True
'''
