git pull

rm -rf manuscript
mdkir manuscript

cp -r /Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/manuscripts/owned manuscript

git add .
git commit -m "latest update"
git push