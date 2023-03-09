from math import ceil

class Zipzap():
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1:
            return s
        
        n = len(s)

        # The method ceil(x) in Python returns a ceiling value of x 
        # i.e., the smallest integer greater than or equal to x.
        sections = ceil(n / (2 * num_rows - 2.0))
        num_cols = sections * (num_rows - 1)
        
        matrix = [[' '] * num_cols for _ in range(num_rows)]
        
        curr_row, curr_col = 0, 0
        curr_string_index = 0
        
        # Iterate in zig-zag pattern on matrix and fill it with string characters.
        while curr_string_index < n:
            # Move down.
            while curr_row < num_rows and curr_string_index < n:
                matrix[curr_row][curr_col] = s[curr_string_index]
                # move downward
                curr_row += 1
                curr_string_index += 1
                
            # skip two rows and one column
            curr_row -= 2
            curr_col += 1
            
            # Move up (with moving right also).
            while curr_row > 0 and curr_col < num_cols and curr_string_index < n:
                matrix[curr_row][curr_col] = s[curr_string_index]
                # move upward
                curr_row -= 1
                curr_col += 1
                curr_string_index += 1
        
        answer = ""
        for row in matrix:
            answer += "".join(row)
            
        return answer.replace(" ", "")

my = Zipzap()
print(my.convert('ThisIsATestInTheFinalExamination',4))