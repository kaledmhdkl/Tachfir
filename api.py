from flask import Flask, request, jsonify

app = Flask(__name__)

dec = [ '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '8a', '8b', '8c', '8d', '8e', '8f', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '9a', '9b', '9c', '9d', '9e', '9f', 'a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'aa', 'ab', 'ac', 'ad', 'ae', 'af', 'b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'ba', 'bb', 'bc', 'bd', 'be', 'bf', 'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'ca', 'cb', 'cc', 'cd', 'ce', 'cf', 'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'da', 'db', 'dc', 'dd', 'de', 'df', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'ea', 'eb', 'ec', 'ed', 'ee', 'ef', 'f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'fa', 'fb', 'fc', 'fd', 'fe', 'ff']
x = [ '1','01', '02', '03', '04', '05', '06', '07', '08', '09', '0a', '0b', '0c', '0d', '0e', '0f', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1a', '1b', '1c', '1d', '1e', '1f', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '2a', '2b', '2c', '2d', '2e', '2f', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '3a', '3b', '3c', '3d', '3e', '3f', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '4a', '4b', '4c', '4d', '4e', '4f', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '5a', '5b', '5c', '5d', '5e', '5f', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '6a', '6b', '6c', '6d', '6e', '6f', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7a', '7b', '7c', '7d', '7e', '7f']


def Decrypt_ID(da):
    if da and len(da) == 10:
        w= 128
        xxx =len(da)//2-1
        for i in range(int(xxx)-1):
            w =w*128
        x1 =da[:2]
        x2 =da[2:4]
        x3 =da[4:6]
        x4 =da[6:8]
        x5 =da[8:10]
        return str(w*x.index(x5)+(dec.index(x2)*128)+dec.index(x1)+(dec.index(x3)*128*128)+(dec.index(x4)*128*128*128))
    if da and len(da) == 8:
        w= 128
        xxx =len(da)//2-1
        for i in range(int(xxx)-1):
            w =w*128
        x1 =da[:2]
        x2 =da[2:4]
        x3 =da[4:6]
        x4 =da[6:8]
        return str(w*x.index(x4)+(dec.index(x2)*128)+dec.index(x1)+(dec.index(x3)*128*128))    
    return None 


def Encrypt_ID(num):
    num = int(num)
    xxx= [ '1','01', '02', '03', '04', '05', '06', '07', '08', '09', '0a', '0b', '0c', '0d', '0e', '0f', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1a', '1b', '1c', '1d', '1e', '1f', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '2a', '2b', '2c', '2d', '2e', '2f', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '3a', '3b', '3c', '3d', '3e', '3f', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '4a', '4b', '4c', '4d', '4e', '4f', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '5a', '5b', '5c', '5d', '5e', '5f', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '6a', '6b', '6c', '6d', '6e', '6f', '70', '71', '72', '73', '74', '75', '76', '77', '78', '79', '7a', '7b', '7c', '7d', '7e', '7f']
    num = num/128 
    if num>128:
        num =num/128
        if num >128:
            num= num/128
            if num>128:
                num= num/128
                strx= int(num)
                y= (num-int(strx))*128
                z = (y-int(y))*128
                n =(z-int(z))*128
                m=(n-int(n))*128
                return dec[int(m)]+dec[int(n)]+dec[int(z)]+dec[int(y)]+xxx[int(num)]
            else:
                strx= int(num)
                y= (num-int(strx))*128
                z = (y-int(y))*128
                n =(z-int(z))*128
                return dec[int(n)]+dec[int(z)]+dec[int(y)]+xxx[int(num)]
    return None


@app.route("/encrypt")
def api_encrypt():
    num = request.args.get("id")
    if not num:
        return jsonify({"error": "Missing id param"}), 400
    try:
        enc = Encrypt_ID(num)
        return jsonify({"id": num, "encrypted": enc})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/decrypt")
def api_decrypt():
    da = request.args.get("da")
    if not da:
        return jsonify({"error": "Missing da param"}), 400
    try:
        dec_ = Decrypt_ID(da)
        return jsonify({"da": da, "decrypted": dec_})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Encrypt/Decrypt API",
        "routes": {
            "/encrypt?id=NUMBER": "Encrypt ID",
            "/decrypt?da=HEXSTRING": "Decrypt DA"
        }
    })
