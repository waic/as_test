#!/usr/local/bin/perl

# settings
# クエリの名前。H32-2 では 'dest' となっている
my $param_name = 'dest';

# リダレイクト先のprefix
# 渡された値を連結する。末尾の / は省略可能、あっても良い
# H32-2 を見ると、渡される値の先頭には / がつく想定だが、なくても問題ないようにする (セキュリティ上の理由)。
my $redirect_uri_prefix = 'https://waic.github.io/as_test/WAIC-CODE/';

# クエリ読む
my $buffer;
if ($ENV{'REQUEST_METHOD'} eq "POST") {
	read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
}else {
	$buffer = $ENV{'QUERY_STRING'};
}
my $pair;
foreach $pair (split(/[&;]/,$buffer)){
	my($name, $value) = split(/=/, $pair);
	$value =~ tr/+/ /;
	$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	$FORM{$name} = $value;
}

# 値の取得とチェック
my $uri_path = $FORM{$param_name};
if(!$uri_path){
	&message('パスを指定してください。');
	exit;
}
if($uri_path !~ m|^/?[-_A-Za-z0-9]+\.html?$|o){
	&message('指定されたパスにはリダイレクトできません。') ;
	exit;
}

# URLを作成
# 連結する文字の先頭・末尾の / を取り除く
$redirect_uri_prefix =~ s|/$||;
$uri_path =~ s|^/||;

# / をはさむ
my $redirect_uri = $redirect_uri_prefix . '/' . $uri_path;


#302
print <<"_EndOfText_";
Status: 302 Found
Location: $redirect_uri
Content-type: text/html; charset=UTF-8
Content-Language: ja
Pragma: no-cache
Cache-Control: no-cache

<!DOCTYPE html>
<html lang="ja">
<head>
<title>302 found</title>
</head>
<body>
<p><a href="$redirect_uri">$redirect_uri</a></p>
</body>
</html>
_EndOfText_
exit;


# エラー表示
sub message{
	my $message = $_[0];

	print <<"_EndOfText_";
Content-type: text/html; charset=UTF-8
Content-Language: ja
Pragma: no-cache
Cache-Control: no-cache

<!DOCTYPE html>
<html lang="ja">
<head>
<title>Error</title>
</head>
<body>
<h1>Error</h1>
<p>$message</p>
</body>
</html>
_EndOfText_
}
