import javax.swing.*;
import java.awt.*;

public class DataLineageMap extends JFrame {

    public DataLineageMap() {
        setTitle("Data Lineage Diagram");
        setSize(800, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JPanel mapPanel = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);

                // ... (code to draw boxes and labels)

                // Draw arrows for data flow
                drawArrow(g, 150, 225, 250, 225); // User to Web Server
                g.drawString("username, password", 170, 215);
                drawArrow(g, 350, 225, 450, 225); // Web Server to Database
                g.drawString("auth data", 370, 215);
            }
        };

        add(mapPanel);
        setVisible(true);
    }

    // Helper function to draw arrows (moved outside the JPanel)
    private void drawArrow(Graphics g, int x1, int y1, int x2, int y2) {
        int dx = x2 - x1, dy = y2 - y1;
        double D = Math.sqrt(dx * dx + dy * dy);
        double xm = D - 10, xn = xm, ym = 5, yn = -5, x;
        double sin = dy / D, cos = dx / D;

        x = xm * cos - ym * sin + x1;
        ym = xm * sin + ym * cos + y1;
        xm = x;

        x = xn * cos - yn * sin + x1;
        yn = xn * sin + yn * cos + y1;
        xn = x;

        int[] xpoints = { x2, (int) xm, (int) xn };
        int[] ypoints = { y2, (int) ym, (int) yn };

        g.drawLine(x1, y1, x2, y2);
        g.fillPolygon(xpoints, ypoints, 3);
    }

    public static void main(String[] args) {
        new DataLineageMap();
    }
}