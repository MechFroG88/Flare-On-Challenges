// Online C# Editor for free
// Write, Edit and Run your C# code using C# Online Compiler

using System;

public class HelloWorld
{
    public static void Main(string[] args)
    {
        byte[] dat_secret = {0xa1,0xb5,0x44,0x84,0x14,0xe4,0xa1,0xb5,0xd4,0x70,0xb4,0x91,0xb4,0x70,0xd4,0x91,0xe4,0xc4,0x96,0xf4,0x54,0x84,0xb5,0xc4,0x40,0x64,0x74,0x70,0xa4,0x64,0x44};
		string text = "";
		foreach (byte b in dat_secret)
		{
			text += (char)(((uint)(b >> 4) | ((uint)(b << 4) & 0xF0u)) ^ 0x29u);
		}
		text += "\0";
		string text2 = "";
		for (int j = 0; j < text.Length; j += 2)
		{
			text2 += text[j + 1];
			text2 += text[j];
		}
		Console.WriteLine(text);
		string text3 = "";
		for (int k = 0; k < text2.Length; k++)
		{
			_ = text2[k];
			text3 += (char)((byte)text2[k] ^ 0x66u);
		}
		Console.WriteLine(text3);

        //3rmahg3rd.b0b.d0ge@flare-on.com
    }
}