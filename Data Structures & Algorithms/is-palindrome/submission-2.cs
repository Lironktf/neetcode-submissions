public class Solution {
    public bool IsPalindrome(string s) 
    {
        string cleaned = "";

        foreach(char x in s)
        {
            if(char.IsLetterOrDigit(x)) cleaned += char.ToLower(x);
        }

        int rCounter = cleaned.Length - 1;
        int lCounter = 0;
        while (lCounter < rCounter)
        {
            if(cleaned[lCounter] != cleaned[rCounter]) return false;
            rCounter--;
            lCounter++;
        }    

        return true;
    }
}
