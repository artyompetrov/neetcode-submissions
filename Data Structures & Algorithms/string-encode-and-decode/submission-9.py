class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        if len(strs) == 0:
            return ""
        for s in strs:
            word = []
            for char in s:
                if char == ',':
                    word.append('\\,')
                elif char == '\\':
                    word.append('\\\\')
                else:
                    word.append(char)

            result.append(''.join(word))
        return ','.join(result) + ','

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        result = []
        previous_char_was_encode_symbol = False
        word = []
        for char in s:
            if previous_char_was_encode_symbol:
                if char == ',' or char == '\\':
                    word.append(char) 
                else:
                    raise Error("Unexpected encoded symbol")             
                previous_char_was_encode_symbol = False
            else:
                if char == '\\':
                    previous_char_was_encode_symbol = True
                elif char == ',':
                    result.append(''.join(word))
                    word = []
                else:
                    word.append(char)
        
        return result
                
            
            




