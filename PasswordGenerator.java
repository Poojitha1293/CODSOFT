import javax.swing.*;
import java.awt.*;
import java.util.Random;
import java.awt.datatransfer.*;
import java.awt.Toolkit;

public class PasswordGenerator extends JFrame {

    JTextField usernameField, lengthField, passwordField;
    JLabel label5, label6;

    public PasswordGenerator() {

        setTitle("Password Generator");
        setSize(1200, 700);
        setLayout(null);
        getContentPane().setBackground(Color.WHITE);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        JLabel title = new JLabel("PASSWORD GENERATOR", JLabel.CENTER);
        title.setFont(new Font("Goudy Old Style", Font.BOLD, 30));
        title.setOpaque(true);
        title.setBackground(Color.GREEN);
        title.setForeground(Color.WHITE);
        title.setBounds(0, 0, 1200, 80);
        add(title);

        JLabel userLabel = new JLabel("Enter Username");
        userLabel.setFont(new Font("Times New Roman", Font.PLAIN, 20));
        userLabel.setForeground(Color.BLUE);
        userLabel.setBounds(350, 150, 250, 30);
        add(userLabel);

        usernameField = new JTextField();
        usernameField.setFont(new Font("Baskerville Old Face", Font.PLAIN, 20));
        usernameField.setBounds(650, 150, 250, 35);
        add(usernameField);

        JLabel lengthLabel = new JLabel("Enter length of the password");
        lengthLabel.setFont(new Font("Times New Roman", Font.PLAIN, 20));
        lengthLabel.setForeground(Color.BLUE);
        lengthLabel.setBounds(350, 250, 300, 30);
        add(lengthLabel);

        lengthField = new JTextField();
        lengthField.setFont(new Font("Baskerville Old Face", Font.PLAIN, 20));
        lengthField.setBounds(650, 250, 250, 35);
        add(lengthField);

        JButton generateBtn = new JButton("Generate Password");
        generateBtn.setFont(new Font("Baskerville Old Face", Font.BOLD, 15));
        generateBtn.setBackground(Color.RED);
        generateBtn.setBounds(250, 350, 200, 40);
        add(generateBtn);

        JButton acceptBtn = new JButton("Accept Password");
        acceptBtn.setFont(new Font("Baskerville Old Face", Font.BOLD, 15));
        acceptBtn.setBackground(Color.GRAY);
        acceptBtn.setForeground(Color.WHITE);
        acceptBtn.setBounds(480, 350, 200, 40);
        add(acceptBtn);

        JButton resetBtn = new JButton("Reset Password");
        resetBtn.setFont(new Font("Baskerville Old Face", Font.BOLD, 15));
        resetBtn.setBackground(Color.ORANGE);
        resetBtn.setBounds(710, 350, 200, 40);
        add(resetBtn);

        JButton copyBtn = new JButton("Copy Password");
        copyBtn.setFont(new Font("Baskerville Old Face", Font.BOLD, 15));
        copyBtn.setBackground(Color.PINK);
        copyBtn.setBounds(940, 350, 200, 40);
        add(copyBtn);

        JLabel passwordLabel = new JLabel("Generated Password");
        passwordLabel.setFont(new Font("Times New Roman", Font.PLAIN, 20));
        passwordLabel.setForeground(Color.BLUE);
        passwordLabel.setBounds(350, 450, 250, 30);
        add(passwordLabel);

        passwordField = new JTextField();
        passwordField.setFont(new Font("Baskerville Old Face", Font.PLAIN, 20));
        passwordField.setBounds(650, 450, 300, 35);
        add(passwordField);

        label5 = new JLabel();
        label5.setFont(new Font("Baskerville Old Face", Font.PLAIN, 18));
        label5.setBounds(350, 500, 800, 30);
        add(label5);

        label6 = new JLabel();
        label6.setFont(new Font("Baskerville Old Face", Font.PLAIN, 18));
        label6.setBounds(350, 550, 800, 30);
        add(label6);

        // Generate Password
        generateBtn.addActionListener(e -> {
            try {
                if (usernameField.getText().isEmpty()) {
                    JOptionPane.showMessageDialog(this,
                            "Please Enter User Name!",
                            "Warning",
                            JOptionPane.WARNING_MESSAGE);
                } else if (lengthField.getText().isEmpty()) {
                    JOptionPane.showMessageDialog(this,
                            "Please Enter length of the Password!",
                            "Warning",
                            JOptionPane.WARNING_MESSAGE);
                } else {
                    int length = Integer.parseInt(lengthField.getText());
                    String chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+";
                    Random random = new Random();
                    StringBuilder password = new StringBuilder();

                    for (int i = 0; i < length; i++) {
                        password.append(chars.charAt(random.nextInt(chars.length())));
                    }
                    passwordField.setText(password.toString());
                }
            } catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(this,
                        "Please enter a valid integer!",
                        "Error",
                        JOptionPane.ERROR_MESSAGE);
            }
        });

        // Accept Password
        acceptBtn.addActionListener(e -> {
            if (passwordField.getText().isEmpty()) {
                JOptionPane.showMessageDialog(this,
                        "Please Generate Password to Accept it",
                        "Generate password!",
                        JOptionPane.WARNING_MESSAGE);
            } else {
                label5.setText("Hi " + usernameField.getText()
                        + "! Your Password is : " + passwordField.getText());
            }
        });

        // Reset
        resetBtn.addActionListener(e -> {
            usernameField.setText("");
            lengthField.setText("");
            passwordField.setText("");
            label5.setText("");
            label6.setText("");
        });

        // Copy Password
        copyBtn.addActionListener(e -> {
            if (!passwordField.getText().isEmpty()) {
                StringSelection selection = new StringSelection(passwordField.getText());
                Clipboard clipboard = Toolkit.getDefaultToolkit().getSystemClipboard();
                clipboard.setContents(selection, selection);
                label6.setText("Copied Password is : " + passwordField.getText());
            } else {
                JOptionPane.showMessageDialog(this,
                        "Please generate the Password to Copy!",
                        "Error",
                        JOptionPane.ERROR_MESSAGE);
            }
        });

        setVisible(true);
    }

    public static void main(String[] args) {
        new PasswordGenerator();
    }
}
