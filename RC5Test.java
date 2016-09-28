package rc5.test;

import java.io.BufferedOutputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.security.GeneralSecurityException;
import java.security.InvalidAlgorithmParameterException;
import java.security.InvalidKeyException;
import java.security.Key;
import java.security.NoSuchAlgorithmException;
import java.security.NoSuchProviderException;
import java.security.SecureRandom;
import java.security.Security;
import java.security.spec.AlgorithmParameterSpec;
import java.security.spec.KeySpec;
import java.util.Arrays;
import java.util.Scanner;
import java.util.regex.Pattern;
import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.KeyGenerator;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.SecretKey;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.RC5ParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import org.bouncycastle.jce.provider.BouncyCastleProvider;

public class RC5Test {
    
    public static void main(String[] args) {
        boolean BCInstalled = false;
        Security.addProvider(new BouncyCastleProvider());
        if (Security.getProvider("BC") == null){
            System.out.println("No avaliable");
        }
        else{
            BCInstalled = true;
            System.out.println("Avaliable");
        }
        if (BCInstalled){
            test2();
        }
    }
    
    private static void test2(){
        try {
            String provider = "BC";
            byte[] keyBytes = {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00};
            Key key = new SecretKeySpec(keyBytes, "RC5");

            byte[] IV = {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00};
            AlgorithmParameterSpec IVspec = new IvParameterSpec(IV);

            Cipher cipher = Cipher.getInstance("RC5/CBC/PKCS7PADDING", provider);
            cipher.init(Cipher.DECRYPT_MODE, key, IVspec);

            byte[] encryptedData = {(byte)0xf7, (byte)0x84, (byte)0x54, (byte)0xf4, (byte)0xc5, (byte)0x23, (byte)0xeb, (byte)0xb3,
                                    (byte)0xf0, (byte)0x7d, (byte)0x42, (byte)0xc5, (byte)0xf8, (byte)0x99, (byte)0x4c, (byte)0xfa,
                                    (byte)0x2f, (byte)0x28, (byte)0x16, (byte)0x78, (byte)0xcf, (byte)0x45, (byte)0xa7, (byte)0x02,
                                    (byte)0x7a, (byte)0x85, (byte)0x74, (byte)0x19, (byte)0x30, (byte)0x85, (byte)0x53, (byte)0x4c,
                                    (byte)0x97, (byte)0x89, (byte)0xba, (byte)0x80, (byte)0x82, (byte)0x73, (byte)0xec, (byte)0xdb};
            
            // 0x28, 0xc6, 0x41, 0x1c, 0x35, 0x80, 0x56, 0x49
             byte[] oracleData = {(byte)0x20, (byte)0xce, (byte)0x49, (byte)0x14, (byte)0x3d, (byte)0x88, (byte)0x5e, (byte)0x41,
                                  (byte)0x97, (byte)0x89, (byte)0xba, (byte)0x80, (byte)0x82, (byte)0x73, (byte)0xec, (byte)0xdb};

            byte[] data = cipher.doFinal(oracleData);
            
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < data.length; i++) {
                if (i > 0 && (i % 8) == 0){
                    sb.append(String.format("| "));
                }
                sb.append(String.format("%02X ", data[i]));
            }
            System.out.println(sb);
        } 
        catch(NoSuchAlgorithmException | 
                NoSuchPaddingException | 
               NoSuchProviderException | 
                   InvalidKeyException | 
                   BadPaddingException | 
             IllegalBlockSizeException |
    InvalidAlgorithmParameterException ex){
            System.out.println(ex.getMessage());
        }
    }
    
    private static void test(){
        String provider = "BC";
        try{
            byte[] keyBytes = {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00};
            Key key = new SecretKeySpec(keyBytes, "RC5");
            
            byte[] IV = {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00};
            AlgorithmParameterSpec IVspec = new IvParameterSpec(IV);
            //KeyGenerator keyGenerator = KeyGenerator.getInstance("RC5", provider);
            //SecretKey secretKey = keyGenerator.generateKey();
            //byte[] IV = {0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00};
            
            Cipher cipher = Cipher.getInstance("RC5/CBC/PKCS7PADDING", provider);
            cipher.init(Cipher.ENCRYPT_MODE, key, IVspec);
            
            StringBuilder sb;
            byte[] data = "Hello World of Encryption using RC5".getBytes();
            sb = new StringBuilder();
            for (int i = 0; i < data.length; i++) {
                if (i > 0 && (i % 8) == 0){
                    sb.append(String.format("| "));
                }
                sb.append(String.format("%02X ", data[i]));
            }
            System.out.println(sb);
//            FileOutputStream outputStream = null;
//            File dataFile = new File("data_file.txt");
//            outputStream = new FileOutputStream(dataFile);
//            outputStream.write(data);
//            outputStream.close();
            
            byte[] encryptedData = cipher.doFinal(data);
            sb = new StringBuilder();
            for (int i = 0; i < encryptedData.length; i++) {
                if (i > 0 && (i % 8) == 0){
                    sb.append(String.format("| "));
                }
                sb.append(String.format("%02X ", encryptedData[i]));
            }
//            File encryptedFile = new File("encrypted_file.txt");
//            outputStream = new FileOutputStream(encryptedFile);
//            outputStream.write(encryptedData);
//            outputStream.close();
            System.out.println(sb);
        }
        catch(NoSuchAlgorithmException | 
                NoSuchPaddingException | 
               NoSuchProviderException | 
                   InvalidKeyException | 
                   BadPaddingException | 
             IllegalBlockSizeException |
    InvalidAlgorithmParameterException ex){
            System.out.println(ex.getMessage());
        }
    }
    
}
