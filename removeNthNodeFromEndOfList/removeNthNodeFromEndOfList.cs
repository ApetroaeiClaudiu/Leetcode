/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    
    public int count(ListNode head) {
        int count = 0;

        while(head != null) {
            count++;
            head = head.next;
        }

        return count;
    }

    public ListNode RemoveNthFromEnd(ListNode head, int n) {
        
        if ( n == 0) {
            return head;
        }

        int count = this.count(head);
        int poz = count - n;
        if ( poz == 0) {
            head = head.next;
            return head;
        }
        ListNode temp = head;
        int index = 0 ;

        while (index < poz - 1) {
            index++;
            temp = temp.next;
        }
        temp.next = temp.next.next;

        return head;
    }

}
