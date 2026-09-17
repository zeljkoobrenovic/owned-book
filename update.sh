git pull

rm -rf manuscript
mdkir manuscript
mdkir manuscript/resources
cp title_page.jpg manuscript/resources

cp -r /Users/zeljkoobrenovic/PycharmProjects/spec-driven-journals/manuscripts/owned manuscript

git add .
git commit -m "latest update"
git push

