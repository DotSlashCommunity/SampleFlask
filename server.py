from flask import Flask, jsonify, request, send_from_directory

# the flask app
app = Flask(__name__)

# global
ans = 0.0

@app.route("/")
def _serve():
  return send_from_directory(".", "index.html")

@app.route("/solve")
def _solve():
  global ans

  args = request.args

  # ensure there is a e
  if "e" not in args.keys():
    return jsonify({
        "ok": False,
        "msg": "MissingExpr"
      })

  # ensure non empty
  if args["e"] in ["", None]:
    return jsonify({
        "ok": False,
        "msg": "EmptyExpr"
      })

  try:
  
    ans = eval(args["e"])
    return jsonify({
        "ok": True,
        "ans": ans
      })

  except SyntaxError:
    return jsonify({
        "ok": False,
        "msg": "SyntaxErr"
      })

  except NameError:
    return jsonify({
        "ok": False,
        "msg": "NameErr"
      })

if __name__ == "__main__":
  app.run("0.0.0.0", debug=True)
