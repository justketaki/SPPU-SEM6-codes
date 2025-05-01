public class LinearSearch {
    public static void linearSearch(Integer key) {  
        List<Integer> lon = new List<Integer>{3, 4, 5, 6, 7, 8};
        Boolean found = false;  // Flag to track if the element is found
        
        for (Integer i = 0; i < lon.size(); i++) {
            if (lon[i] == key) {
                found = true;
                System.debug('Element Found at index: ' + i); 
                break; // Exit the loop once the element is found
            }
        }
        
        if (!found) {
            System.debug('Element Not Found: ' + key);
        }
    }
}

//LinearSearch.linearSearch(10);
